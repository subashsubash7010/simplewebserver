<!doctype html>
<html>
<head>
<title> My laptop configurationr</title>
</head>
<body align="center"><h1>My laptop configuration</h1>
<table border="5" align="center">
    <tr>
        <th>
            laptop configuration
        </th>
        <th>
            description
        </th>
    <tr>
        <td>
            device name
        </td>
        <td>
            subash
        </td>
    </tr>
    <tr>
        <td>processor
        </td>
        <td>AMD Ryzen 7 7435 HS
        </td>
    <tr>
        <td>Installed RAM
        </td>
        <td>
            16.0 GB (15.8 GB usable)
        </td>
    </tr>
    <tr>
        <td>
            Device ID
        </td>
        <td>
            ABB73E06-F358-4E25-90B3-4221AC47C913
        </td>
    </tr>
    <tr>
        <td>
            Product ID
        </td>
        <td>00342-42702-88379-AAOEM</td>
    </tr>
    <tr>
        <td>
            System Type
        </td>
        <td>64-bit operating system, x64-based processor</td>
    </tr>
</table>
</body>
</html>


class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        print("Get request received...")
        self.send_response(200) 
        self.send_header("content-type", "text/html")       
        self.end_headers()
        self.wfile.write(content.encode())

print("This is my webserver") 
server_address =('',8000)
httpd = HTTPServer(server_address,MyServer)
httpd.serve_forever()