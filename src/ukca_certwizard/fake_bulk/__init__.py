import typer

app = typer.Typer()

@app.command()
def renew(cert_config: typer.Argument(..., help="Configuration listing certificates to renew")):
    """Renew the certificate"""
    pass

@app.command()
def request(cert_config: str):
    """Request a certificate"""
    pass

@app.command()
def retrieve(cert_config: str):
    """Retrieve the certificate"""
    pass