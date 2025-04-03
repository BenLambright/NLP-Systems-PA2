import notebook

if __name__ == '__main__':
    app = notebook.create_app()
    app.run(host='0.0.0.0', port=5000, debug=True)  # added the host and port so that we can call -p to redirect it locally when containerized