import typer
import os
import shutil


os.chdir('C:/Users/charles/Desktop/aok assets')

app = typer.Typer()


@app.command()
def bot():
    os.mkdir('qoutes')


if __name__ == "__main__":
    app()
