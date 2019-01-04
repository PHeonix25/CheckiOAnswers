import click

@click.group()
def checkioanswers():
    pass

@checkioanswers.command()
def cmd1():
    '''Command on checkioanswers'''
    click.echo('checkioanswers cmd1')

@checkioanswers.command()
def cmd2():
    '''Command on checkioanswers'''
    click.echo('checkioanswers cmd2')

if __name__ == '__main__':
    checkioanswers()
