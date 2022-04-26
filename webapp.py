import justpy as jp


def app():
    wp = jp.QuasarPage()
    #creating object for each element
    wp = jp.QuasarPage(a=wp, text='Analysis of Course Reviews')
    h1 = jp.QDiv(a=wp, text="These graphs course review analysis")
    return wp

jp.justpy(app)