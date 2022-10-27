| Method          | Local | Same-Zone | Different Region |
|-----------------|-------|-----------|------------------|
| ---             | ---   | ---       | ---              |
| REST add        | 2.58  | 2.60      | 286.43           |
| gRPC add        | .049  | .53       | 145.03           |
| REST rawimg     | 4.90  | 7.86      | 1170.29          |
| gRPC rawimg     | 8.84  | 10.11     | 190.82           |
| REST dotproduct | 4.09  | 4.04      | 287.29           |
| gRPC dotproduct | .60   | .65       | 144.97           |
| REST jsonimg    | 49.9  | 60.29     | 1353.75          |
| gRPC jsonimg    | 22.7  | 25.64     | 214.41           |
| PING            | .05   | .37       | 141.59           |

My results are a strong argument for gRPC, especially across large distances.
It is clear in the results from the small "add" call that repeated requests via gRPC have very little overhead, while the REST calls are burdened with the time required to make each connection, in addition to the time needed for data to travel back and forth.
At short distances (local vs same zone) the TCP connection time is negligible compared to the time that the medium size REST queries take, especially dot product and add. With more complex queries, and larger distances, the differences become more significant. It's particularly impressive that gRPC handles the image requests in about the same time as the simple math requests across large distances.
