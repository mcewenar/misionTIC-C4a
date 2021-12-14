const { gql } = require('apollo-server');

const productsTypeDefs = gql `
    type Product {
        id_products: Int!
        name_product: String!
        description: String        
        price: String!
        stock: Int!
        type_product: Int!
        photos: [Photo]
    }

    type Photo{
        id : Int
        name: String!
        product: Int!
        image: String!
    }

    type Type{
        id: Int
        name: String!
    }

    input ProductInput {
        id_products: Int!
        name_product: String!
        price: Float!
        stock: Int!
        type_product: Int!
    }
    
    input TypeInput {        
        name: String!
    }

    extend type Query {
        productsByType(type_product: Int!): [Product]
        productPhotos(products_id: Int!): [Photo]
        productsTypes: [Type]
        productById(products_id: Int!): Product
    }
    extend type Mutation {
        createProduct(product: ProductInput!): Product
        createType(type: TypeInput!): Type
    }
`;
module.exports = productsTypeDefs;