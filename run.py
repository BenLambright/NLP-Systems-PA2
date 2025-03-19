import notebook

if __name__ == '__main__':
    app = notebook.create_app()
    app.run(debug=True)
