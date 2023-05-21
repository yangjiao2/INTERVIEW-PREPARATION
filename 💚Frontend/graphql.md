1/ Reducing overhead of GraphQL layer
GraphQL queries are usually delivered over HTTP protocol. The difference between REST queries and GraphQL queries is that GraphQL payload will contain both data + metadata required to make the query. Metadata for queries tend to be larger than the data query. Server needs to understand provided metadata (called document) by parsing it. Parsing metadata into GraphQL AST can be expensive but also can be avoided in cases where developers care about performance and use limited set of graphql queries in their applications.

There are numerous packages that offer document cache on top of the GraphQL-express/GraphQL-JS. For example, GraphQL-JIT will allow precompiling graphql documents reducing amount of time required to process


2/ data loader!
DataLoading problem is not strictly related to GraphQL. In fact, every RESTfull API that utilizes ORM will have similar problems. That is why many developers prefer to write complex data queries (yes yes.. involving SQL Joins or Map Reduce) for REST over the ORM layer. ORM layers usually come with the cache layer that can be configured to resolve this problem.

GraphQL implementation will build a query execution plan that will trigger different resolvers that individually can perform different data queries.
Multiple data queries for the same resource can be avoided that is why data loader library was built:

graphql/dataloader
