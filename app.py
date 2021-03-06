import muffin


app = muffin.Application('app')


@app.register('/', '/hello/{name}')
def hello(request):
    name = request.match_info.get('name', 'anonymous')
    return 'Hello %s!' % name


if __name__ == '__main__':
    app.manage()
