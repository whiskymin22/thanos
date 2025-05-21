FROM node:16 as build

WORKDIR /app

# Copy package.json and package-lock.json
COPY package.json ./ 
COPY package-lock.json ./  

# Install dependencies
RUN npm install --legacy-peer-deps  # Use --legacy-peer-deps to avoid dependency conflicts

# Copy the application code
COPY . .

# Build the React app for production
RUN npm run build

# Production environment
FROM nginx:stable-alpine
COPY --from=build /app/build /usr/share/nginx/html
COPY nginx.conf /etc/nginx/conf.d/default.conf

EXPOSE 3000

CMD ["nginx", "-g", "daemon off;"]

