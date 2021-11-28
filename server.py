def render_template(template="index.html", path="/", context={}):
    html_str = ""
    with open(template, 'r') as f:
        html_str = f.read()
        html_str = html_str.format(**context)
    return html_str

def home(environ):
    return render_template(template="index.html", context={})

def contact_us(environ):
    return render_template(template="contact.html", context={})

def app(environ, start_response):
    path = environ.get("PATH_INFO")
    if path.endswith("/"):
        path = path[:-1]
    if path == "":
        data = home(environ)
    elif path == "/contact":
        data = contact_us(environ)
    else:
        data = render_template(template="404.html", context={"path": path})
    data = data.encode("utf-8")
    start_response(
        f"200 OK", [
            ("Content-Type", "text/html"),
            ("Content-Type", str(len(data)))
        ]
    )

    return iter([data])