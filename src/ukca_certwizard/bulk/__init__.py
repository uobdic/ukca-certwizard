import typer

app = typer.Typer()

@app.command()
def renew():
    """Renew the certificate"""
    pass

@app.command()
def request():
    """Request a certificate"""
    pass

@app.command()
def retrieve():
    """Retrieve the certificate"""
    pass