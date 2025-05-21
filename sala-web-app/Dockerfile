# Use a specific Node.js base image
FROM node:16-alpine

# Set the working directory inside the container
WORKDIR /app

# Copy package.json and package-lock.json (or yarn.lock)
COPY package*.json ./

# Install dependencies
RUN npm install

# Copy the source code into the container and change ownership
COPY --chown=node:node . .

# Build the application (if necessary)
RUN npm run build

# Expose the port the app runs on
EXPOSE 3000

# Command to start the application, using environment variables if needed
CMD ["npm", "start"]
