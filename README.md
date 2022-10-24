[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-c66648af7eb3fe8bc4f294546bfd86ef473780cde1dea487d3c4ff354943c9ae.svg)](https://classroom.github.com/online_ide?assignment_repo_id=9051713&assignment_repo_type=AssignmentRepo)
# Lab6 - Comparing REST and gRPC remote procedure calls.
This lab designed to help you understand the programmatic and performance difference between REST and gRPC APi's. You will develop a REST and a gRPC api then compare the performance for latency / bandwidth.

## API endpoints / services

If you haven't done this already, you should go through [the simple flask rest-server tutorial](https://github.com/cu-csci-4253-datacenter/simple-rest-server-tutorial) we covered earlier.

You need to extend a server and client for the REST and gRPC services. Part of the REST server and a prototype client has been provided for you because there are some complexities in loading and processing an image in Python; we've provided that for you so you can focus on the REST code.

Our rest service has four endpoints:
* `add` - The first provided service is `add` that takes two integers as parameters on the URL, sums them and returns the sum. This service is designed to emphasize "light weight" remote procedure calls where latency is of paramount concern because the overhead dwarfs the data transmitted or the operation being performed.
* `rawimage` - The second provided service is an `rawImage` service that takes an image (in JPG or PNG format) and returns the `width` and `height` of the the image. The image is NOT transmitted using JSON -- the payload type is marked as `image/jpg` and the server code retrieves the image using the full payload.
* `dotproduct` - The third service (which you must provide) receives two lists of random numbers, performs a dot-product and then returns that dot product. Given vectors $a$ and $b$, the dot product is $ \sum_i a_i \times b_i $. The service that you implement must accept two vectors of the same length but any length is allowed. The service should accept a JSON object with parameters `a` and `b` which are the lists of numbers. For example, `{ "a" : [ 1, 2], "b" : [3, 4]}` would be an acceptable payload. When testing your code, the client should generate vectors of length 100 and each element should be between 0 and 1 and generated by a `random.random()`. 
* `jsonimage` - The fourth service (which you must provide) does basically the same thing as `rawImage`, but it uses a properly formatted JSON payload rather than an `image/jpg` payload. To do this, you'll need to use the `base64` encoding module to encode the binary data using `base64.encode()`. This turns the binary data into a string which can be part of a valid JSON object. For example `{ "image" : "7636748bdbunchanumbers764764"}` would be an example of a valid object. The routine should return the data results as `rawImage`.

## REST Implementation

File `server.py` is the starter code for the Flask server in Python. 

We've provided the `add` and `rawImage` endpoints. The `rawImage` returns a response containing a JSON document providing the 'width' and 'height' of the image that was provided. The Python Image Library (pillow) is used to process the image.

See `README-REST-details.md` for more details about building the REST API.

## gRPC implementation

We're not providing any starter code for the gRPC implementation. You should [go through the gRPC tutorial](https://grpc.io/docs/tutorials/basic/python/) to walk through the steps of writing a protocol buffers specification that matches the `services` provided by the REST API.

Again, you should construct both a client and a server application where you can run tests for a varying number of times to record the milliseconds needed to perform a single operation.

See `README-gRPC-details.md` for more details about building the gRPC API.

## Conducting your measurements

Once you've gotten your code working, you should create two VM instances (use an `e2-standard-2` instance). Both instances should be in the `us-west1-a` zone (the [documentation on regions and zones is useful here](https://cloud.google.com/compute/docs/regions-zones/#zones_and_clusters)).

> Pro Tip:
> This could a great time to create an instance, configure the instance by installing the needed python libraries, take a snapshot and then create the second instance from the snapshot. Or, you can use your lab5 snapshot which already has Flask installed.


For the first test, you should run the server and client code on the same host, specifying 'localhost' as the endpoint. If you run about 1000 queries, you should find that the REST code takes ~2ms per add query.

For the second test, you should run the server and client on different hosts within the same zone. You should find that the REST code takes about the same time as the localhost implementation.

For the *third* test, you should create a new server in the `europe-west3-a` zone (Frankfurt) and test the client/server speed. You may need to adjust the numbe of repitions you measure based on the latency you encounter). You'll find that the REST add api takes ~270ms rather than 2ms. You may need to adjust the number of repititions you do to keep the running time managable (do at least 100 resp).

In each case, you should use the **internal IP address** rather than than the external IP address for the hosts (i.e. a 10.x.y.z address)

Then, repeat the same three measurements using the gRPC method.

When you're done, edit a file `SOLUTION.md` that includes a table showing the time per-method for each of the RPC mechanisms as below.


|  Method 	| Local  	| Same-Zone  	|  Different Region 	|
|---	|---	|---	|---	|---	|
|   REST add	|   	|   	|  	|
|   gRPC add	|   	|   	|    	|
|   REST rawimg	|   	|   	|   	|
|   gRPC rawimg	|       |   	|   	|
|   REST dotproduct	|   	|   	|  	|
|   gRPC dotproduct	|   	|   	|    	|
|   REST jsonimg	|   	|   	|   	|
|   gRPC jsonimg	|       |   	|   	|
|   PING        |       |      |       |
You should measure the basic latency  using the `ping` command - this can be construed to be the latency without any RPC or python overhead.

You should examine your results and provide a short paragraph with your observations of the performance difference between REST and gRPC as described in `SOLUTIONS.md`.
