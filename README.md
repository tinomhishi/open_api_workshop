# Open API Specifications

Formerly known as the Swagger Specification, is a language agnostinc standard for documenting RestFul API's.
It facilitates collaboration between cross functional teams and provides a common language of communication.

## Why use it?

- Centralized and Integrated Documentation for your API: Provides a single unified file for documenting an entire API,

- Facilitates Collaboration: Allows backend and front-end teams to work in parallel, understanding the API contract even before the api is implemented.

- Enables Automation: Specs can automatically generate client libraries and server stubs, streamlining development.

- Promotes consistency and clarity in API design: Reduces ambiguity and miscommunication

  

### Famous Users

- Stripe
- Paypal
- Twilio

  

### Contract First Development
Open API Specification facilitates Contract-First Development by promoting the idea that the best way to implement an API is to agree on the Specification (Contract) first the programming and business logic comes after.

### Importance of Contract First Development
- Clear initial requirements: Teams agree on API endpoints, request/response formats and error handling prior to development.
- Early feedback: Front End and Backend Team can provide feedback early in the development cycle.
- Scalability: Clear contract improve our ability to scale without breaking functionality.

  
## Key Features

  

### Language Agnostic

OpenApi works with any language. You can define your API without ever having to worry about the implementation on the server or client. Making it easier
to collaborate within teams with different preferences.

### Root Level Fields
- openapi - Defines Open AI version being used
- info - API metadata e.g title, description, version
- servers - API environments
- paths - contains endpoints
- components - reusable objects like schemas, responses, parameters
- security - applicable auth methods like BearerAuth, ApiKeyAuth, BasicAuth, etc.


## Parameters
Elements sent by the client to the server in different parts of an HTTP Request.

### Query Parameters
Appear in the url after the character `?`. For example: `/users?name=tino` 

### Path Parameters
Appear as part of the url. For example: `/department/{dept_id}`

### Header Parameters
Appear in the headers For example: `Authorization: Bearer <token>`

## Request Bodies
The body can contain data in different formats i.e `JSON, XML`. Open AI will allow you to determine their structure.

### Schemas
Models for payload structures

## Responses

Data returned after polling an endpoint

### Status Codes
200 OK, 201 Created, 500 Internal Error, 418 I'm a teapot

### Response Schema
The structure which will define your response

### Error Schema
The structure which will define your response

## Contract First WorkFlow
1. Define Contract - Requirements gathering, API Structure and Data Models. Document Using OpenApi
2. Use The Specification - Generate interactive documentation, Generate Code, Server Stubs
3. Implement API
4. Test and Validate



## Sample Specification

```
openapi: 3.0.0
info:
  title: Product API
  version: "1.0.0"
paths:
  /products:
    get:
      summary: Get all products
      parameters:
        - in: query
          name: in_stock
          schema:
            type: boolean
          description: Filter products by stock availability
      responses:
        "200":
          description: List of products
          content:
            application/json:
              schema:
                type: array
                items:
                  type: object
                  properties:
                    id:
                      type: integer
                    name:
                      type: string
                    price:
                      type: number
                      format: float
                    in_stock:
                      type: boolean
    post:
      summary: Add a new product
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              properties:
                name:
                  type: string
                price:
                  type: number
                  format: float
                in_stock:
                  type: boolean
              required:
                - name
                - price
                - in_stock
      responses:
        "201":
          description: Product created
          content:
            application/json:
              schema:
                type: object
                properties:
                  id:
                    type: integer
                  name:
                    type: string
                  price:
                    type: number
                    format: float
                  in_stock:
                    type: boolean
        "400":
          description: Invalid input
servers:
  - url: http://127.0.0.1:5000
    description: Local Flask Development Server
```

## Additional Reading and Tools
- https://swagger.io/tools/swagger-ui/
- https://editor.swagger.io/
- https://swagger.io/tools/swagger-codegen/
- https://openapi-generator.tech/
