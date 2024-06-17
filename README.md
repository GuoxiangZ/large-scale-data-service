# Project High-level Design

## Project Overview
This project aims to create a web application that displays data entries with the following attributes: id, date, catalog, and name. The application will use AWS services (Lambda and DynamoDB) for backend processing and React for the frontend.

## Functional and Non-functional Requirement
- Functional req:
  - The frontend should display a table of data entries, each with id, date, catalog, and name attributes.
  - Users should be able to filter data based on catalog and date.
- Non-functional req:
  - The system should have high availability and reliability, ensuring data is not lost and service is uninterrupted.
  - The functionality and display of this application should be intuitive enough for users to easily understand.
  - The application's UI should be aesthetically pleasing.

## High-level design
![Design](https://github.com/GuoxiangZ/large-scale-data-service/blob/main/image/8131718594734_.pic.jpg)

- React Table: For creating and managing tables.
- Ant Design: Another UI library with a rich set of components.
- Axios: For making HTTP requests.
- Formik: To check if the input for filters are legal.

## large-scala-data-service project notes
## NoSQL database?
- 定义：当人们使用术语“NoSQL 数据库”时，他们通常用它来指代任何非关系数据库。
- 特点：
  - NoSQL数据库不需要预定义表结构（schema-free）
  - NoSQL 数据库允许开发人员存储大量非结构化数据，从而赋予他们很大的灵活性。
 
## NoSQL 数据库的类型：
- 文档数据库将数据存储在类似于 JSON（JavaScript 对象表示法）对象的文档中。每个文档包含字段和值对。值通常可以是多种类型，包括字符串、数字、布尔值、数组或对象等。

- 键值数据库是一种更简单的数据库类型，其中每个项目包含键和值。

- 宽列存储将数据存储在表、行和动态列中。

- 图形数据库将数据存储在节点和边中。节点通常存储有关人物、地点和事物的信息，而边则存储有关节点之间关系的信息。

## 与SQL对比
数据模型：
SQL：使用固定表结构（schema），数据以行和列形式存储。

NoSQL：数据模型灵活，不要求预定义表结构，可以存储复杂和嵌套的数据。

查询语言：
SQL：使用结构化查询语言（SQL）进行数据操作。

NoSQL：使用各种不同的查询方法和API，具体取决于数据库类型。

扩展性 scaling：
SQL：垂直扩展，增加硬件性能。

NoSQL：水平扩展，增加服务器数量。

## 要用到的aws产品：
- AWS lambda
- Amazon API Gateway
- Amazon DynamoDB

## Lambda:
AWS Lambda 是一项无服务器事件驱动型计算服务，该服务使您可以运行几乎任何类型的应用程序或后端服务的代码，而无需预置或管理服务器。
