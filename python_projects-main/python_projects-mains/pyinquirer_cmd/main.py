import typer
app = typer.Typer()


@app.command()
def hello(name: str, iq: int, diq: bool = True):
    if diq == False:
        iq = 'cannot be proccesed'
    print(f'hie {name} your iq is {iq}')


@app.command()
def gretting():
    print('goodbye')


if __name__ == "__main__":
    app()
