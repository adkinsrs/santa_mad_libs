# santa_mad_libs
"Letters to Santa" Mad Libs in a Flask-based Web Page running in Docker

This was designed for a work winter holiday party, and I decided to take on the task so that I could practice using Flask

To run the Docker image:

```
docker run -it --rm -p 5000:5000 adkinsrs/santa_mad_libs
```

This will start up the Flask server.  To view the Mad Libs form, point your browser to http://localhost:5000

To stop the Flask server, in the terminal hit Ctrl+C
