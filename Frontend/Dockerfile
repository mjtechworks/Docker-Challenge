# FROM node:16.3.0-alpine

# WORKDIR /
# COPY package*.json ./

# RUN npm i

# COPY . .

# RUN npm run build

# CMD ["npm", "start"]

# base image
# FROM node:lts-alpine

# # set working directory
# WORKDIR /app

# # add `/app/node_modules/.bin` to $PATH
# ENV PATH /app/node_modules/.bin:$PATH

# # install and cache app dependencies
# COPY package*.json ./
# RUN npm ci

# # add app
# COPY . .

# # start app
# CMD ["npm", "run", "dev"]

# # base image
# FROM node:lts-alpine

# # create app directory
# WORKDIR /app

# # copy all files to the container
# COPY . /app/

# # change user to node
# USER node

# # install dependencies
# RUN npm install

# # expose port
# EXPOSE 3000

# # start app
# CMD ["npm", "run", "dev"]

# FROM node:14-alpine3.16
# WORKDIR /app
# COPY package*.json ./
# RUN chown -R node:node /app
# USER node
# RUN npm i --unsafe-perm=true --allow-root
# COPY . .
# CMD ["npm", "start"]

FROM node:16.20-alpine3.17

WORKDIR /app

COPY package*.json ./

RUN node -v

RUN npm -v

RUN rm -rf node_modules && rm -f package-lock.json

RUN curl https://google.com

RUN npm install -f

COPY . .

EXPOSE 3000

CMD ["npm", "start"]

