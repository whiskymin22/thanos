from fastapi import UploadFile
import pandas as pd
from typing import Dict

async def process_excel(file: UploadFile) -> Dict[str, pd.DataFrame]:
    """
    Process the uploaded Excel file and extract data.

    Args:
        file (UploadFile): The uploaded Excel file.

    Returns:
        Dict[str, pd.DataFrame]: A dictionary containing processed DataFrames.
    """
    # Read the Excel file into a pandas DataFrame
    cl_df = pd.read_excel(file.file)

    # Ensure necessary columns exist
    necessary_columns = [
        'uniq_id', 'id', 'company_code', 'document_date', 'document_number', 'description',
        'debit_account', 'credit_account', 'amount', 'partner_code', 'partner_name',
        'business_code', 'material_code', 'material_short_name', 'material_name',
        'item_code', 'item_name'
    ]
    cl_df = cl_df[necessary_columns]

    # Process each section
    revenue_df = process_revenue(cl_df)
    cogs_df = process_cogs(cl_df)
    financials_df = process_financials(cl_df)
    summary_df = generate_summary(revenue_df, cogs_df, financials_df)

    # Return all processed DataFrames
    return {
        "revenue": revenue_df,
        "cogs": cogs_df,
        "financials": financials_df,
        "summary": summary_df
    }

def process_revenue(cl_df: pd.DataFrame) -> pd.DataFrame:
    """
    Process revenue data from the DataFrame.

    Args:
        cl_df (pd.DataFrame): The main DataFrame.

    Returns:
        pd.DataFrame: Processed revenue data.
    """
    revenue_df = cl_df[
        cl_df['credit_account'].astype(str).str.startswith('511') &
        ~cl_df['debit_account'].astype(str).str.startswith(('911', '521', '3332', '333301', '33381'))
    ]

    revenue_df['amount'] = pd.to_numeric(revenue_df['amount'], errors='coerce')
    revenue_df['document_date'] = pd.to_datetime(revenue_df['document_date'], errors='coerce')
    revenue_df['YearMonth'] = revenue_df['document_date'].dt.strftime('%Y-%m')

    # Define revenue categories
    category_filters = {
        "Mall Revenue": revenue_df["business_code"] == "S001",
        "Office Revenue": revenue_df["business_code"] == "S002",
        "Marketing Revenue": revenue_df["business_code"] == "S005",
        "Parking Revenue": revenue_df["business_code"] == "S004",
        "Other Revenue": ~revenue_df["business_code"].isin(["S001", "S002", "S005", "S004"]),
    }

    # Compute revenue by category
    revenue_data = {}
    for category, condition in category_filters.items():
        revenue_data[category] = revenue_df[condition].groupby("YearMonth")["amount"].sum()

    # Convert to DataFrame
    revenue_summary_df = pd.DataFrame(revenue_data).T.fillna(0)
    return revenue_summary_df

def process_cogs(cl_df: pd.DataFrame) -> pd.DataFrame:
    """
    Process COGS (Cost of Goods Sold) data from the DataFrame.

    Args:
        cl_df (pd.DataFrame): The main DataFrame.

    Returns:
        pd.DataFrame: Processed COGS data.
    """
    cogs_df = cl_df[
        cl_df['debit_account'].astype(str).str.startswith('632') &
        ~cl_df['credit_account'].astype(str).str.startswith(('911'))
    ]

    cogs_df['amount'] = pd.to_numeric(cogs_df['amount'], errors='coerce')
    cogs_df['document_date'] = pd.to_datetime(cogs_df['document_date'], errors='coerce')
    cogs_df['YearMonth'] = cogs_df['document_date'].dt.strftime('%Y-%m')

    # Define COGS categories
    category_filters = {
        "Mall COGS": cogs_df["business_code"] == "S001",
        "Office COGS": cogs_df["business_code"] == "S002",
        "Marketing COGS": cogs_df["business_code"] == "S005",
        "Parking COGS": cogs_df["business_code"] == "S004",
        "Other COGS": ~cogs_df["business_code"].isin(["S001", "S002", "S005", "S004"]),
    }

    # Compute COGS by category
    cogs_data = {}
    for category, condition in category_filters.items():
        cogs_data[category] = cogs_df[condition].groupby("YearMonth")["amount"].sum()

    # Convert to DataFrame
    cogs_summary_df = pd.DataFrame(cogs_data).T.fillna(0)
    return cogs_summary_df

def process_financials(cl_df: pd.DataFrame) -> pd.DataFrame:
    """
    Process financial income and expense data.

    Args:
        cl_df (pd.DataFrame): The main DataFrame.

    Returns:
        pd.DataFrame: Processed financial data.
    """
    financial_income_df = cl_df[
        cl_df['credit_account'].astype(str).str.startswith('515') &
        ~cl_df['debit_account'].astype(str).str.startswith('911')
    ]
    financial_expense_df = cl_df[
        cl_df['debit_account'].astype(str).str.startswith('635') &
        ~cl_df['credit_account'].astype(str).str.startswith('911')
    ]

    financial_income_df['amount'] = pd.to_numeric(financial_income_df['amount'], errors='coerce')
    financial_expense_df['amount'] = pd.to_numeric(financial_expense_df['amount'], errors='coerce')

    financial_income_df['YearMonth'] = pd.to_datetime(financial_income_df['document_date']).dt.strftime('%Y-%m')
    financial_expense_df['YearMonth'] = pd.to_datetime(financial_expense_df['document_date']).dt.strftime('%Y-%m')

    financial_data = {
        "Total Financial Income": financial_income_df.groupby("YearMonth")["amount"].sum(),
        "Total Financial Expense": financial_expense_df.groupby("YearMonth")["amount"].sum(),
    }

    return pd.DataFrame(financial_data).T.fillna(0)


def generate_summary(
    revenue_df: pd.DataFrame,
    cogs_df: pd.DataFrame,
    financials_df: pd.DataFrame,
) -> pd.DataFrame:
    """Generate a high level summary of the processed data.

    The summary combines revenue, COGS and financial information to
    provide totals per month as well as the resulting net profit.

    Args:
        revenue_df (pd.DataFrame): Revenue data with categories as index
            and months as columns.
        cogs_df (pd.DataFrame): COGS data with categories as index and
            months as columns.
        financials_df (pd.DataFrame): Financial income/expense with
            categories as index and months as columns.

    Returns:
        pd.DataFrame: A dataframe containing monthly totals and the net
            profit for each month.
    """

    # Totals for each month
    total_revenue = revenue_df.sum(axis=0)
    total_cogs = cogs_df.sum(axis=0)

    # Financial income/expense are already totalled by month in
    # ``financials_df``
    financial_income = financials_df.loc["Total Financial Income"]
    financial_expense = financials_df.loc["Total Financial Expense"]

    # Net profit calculation
    net_profit = total_revenue - total_cogs + financial_income - financial_expense

    summary = pd.DataFrame({
        "Total Revenue": total_revenue,
        "Total COGS": total_cogs,
        "Total Financial Income": financial_income,
        "Total Financial Expense": financial_expense,
        "Net Profit": net_profit,
    }).T.fillna(0)

    return summary

