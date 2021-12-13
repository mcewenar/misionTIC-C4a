const { gql } = require('apollo-server');

const facturaTypeDefs = gql `
    type Product{
        
        name: String!
        amount: Int!
        value: Int!
    }
    type Factura {
        idfactura: String!
        username: String!
        address: String!
        products: [Product!]!
        totalValue: Int!
        date: String!
    }

    input ProductInput{
        
        name: String!
        amount: Int!
        value: Int!
    }
    input FacturaInput {
        username: String!
        address: String!
        products: [ProductInput!]!
        totalValue: Int!
    }

    extend type Query {
        facturaByUsername(username: String!): [Factura]
    }

    extend type Mutation {
        createFactura(factura: FacturaInput!): Factura
    }
`;

module.exports = facturaTypeDefs;