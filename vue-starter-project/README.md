# vue-starter-project

Follow the commands below to set up the front-end:

## Install Node.js
For LINUX:
```
sudo apt update
sudo apt install nodejs
```

For Windows:
Download the installer from node.js website

## Install Vue-CLI
```
npm install -g @vue/cli
```

## Project setup
```
npm install
```

### Compiles and hot-reloads for development: Use this command to start the server to host the application
```
npm run serve
```
After it has compiled successfully, open your browser and naviagte to http://localhost:8080
If you want to make any changes to the application just save them and they should be made automatically to the front-end.

### Compiles and minifies for production: Use this command when you are ready to deploy our beautiful application to the world. 
```
npm run build
```

### Lints and fixes file
```
npm run lint
```

### Axios package install
```
npm install axios
```

### Troubleshooting Notes
When installing these packages, make sure you are in the vue-starter-project directory. If you install them under this directory, and it still is having package issues, install the packages in the distribution packages folder on your machine manually using a command like the following:
```
pip install <package name> --target /path/to/dist-package/folder/
```
The distribution package folder is found in this file path on LINUX:
```
cd /usr/lib/python3/dist-packages/
```

### Customize configuration
See [Configuration Reference](https://cli.vuejs.org/config/).
