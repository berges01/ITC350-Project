const http = require('http');
const { exec } = require('child_process');

http.createServer(function (req, res) {
  if (req.url === '/execute-python') {
    // Execute the Python script
    exec('python /path/to/your/python/script.py', (err, stdout, stderr) => {
      if (err) {
        console.error(`exec error: ${err}`);
        return;
      }
      console.log(`stdout: ${stdout}`);
      console.error(`stderr: ${stderr}`);
    });
    res.writeHead(200, {'Content-Type': 'text/html'});
    res.write('Python script executed');
    res.end();
  } else {
    res.writeHead(404, {'Content-Type': 'text/html'});
    res.end('404 Not Found');
  }
}).listen(8080);