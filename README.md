Post-POST is the only RESTful API HTTP method that primarily operates on resource collections. When creating a subordinate resource in a collection, applying POST to the parent resource prompts it to create a new resource, associate it with the proper hierarchy and return a dedicated URL for later reference.
DELETE-The DELETE method is used to delete a specific resource in a REST API. It is performed by sending a DELETE request to the URL of the resource to be deleted, and the API will remove the resource if it exists
patch-On the other hand, PATCH is used to make a partial update to an existing resource. In other words, if you send a PATCH request to update a resource, the server will only update the specified fields in the existing resource.
get-GET requests are the most common and widely used methods in APIs and websites. Simply put, the GET method is used to retreive data from a server at the specified resource. For example, say you have an API with a /users endpoint. Making a GET request to that endpoint should return a list of all available users.
reason for this code
I have been assigned a project that will be used to manage a system that monitors the status of a set of electronically measured water tanks. The embedded circuit attached to each water tank will measure the height of the water in the tank and report on the tank's current stored volume as a percentage of its maximum capacity.


2trues 1 lie 1
i am black
i am tall
i am in ecse 3038