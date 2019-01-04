import click
import os

@click.group()
@click.option('-v', '--verbose', is_flag=True, default=False, help='Turn verbosity up (useful while debugging)')
def checkioanswers(verbose):
    if (verbose):
        click.echo(click.style('Verbose mode is on', fg='yellow', bold=True))
    pass

@checkioanswers.command()
def list():
    '''List all the answers that I've produced'''
    click.echo('Requested to list all answers')
    for root, dirs, files in os.walk('.'):
        for filename in files:
            if (filename.endswith(".py") and filename[0].isdigit()):
                click.echo("\t" + os.path.join(root, filename))

@checkioanswers.command()
@click.argument('filename')
def run(filename: str):
    '''Given a filename, run the answer.'''
    if (not os.path.isfile(filename)):
        click.echo(click.style('Input provided was not a file', fg='red',bold=True), err=True)
        return

    click.echo('Requested to run \'%s\':' % filename)
    click.echo('')
    exec(open(filename).read(), globals())

    click.echo('')
    click.echo(click.style('File has been run. Exiting now.', fg='green', bold=True))


if __name__ == '__main__':
    checkioanswers()
