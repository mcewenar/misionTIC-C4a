const { gql } = require('apollo-server');
const proveedorTypeDefs = gql `
    type Proveedor {
        name_company: String!
        name_contact: String!
        cel: Int!
        address: String!
        city: String!
        email: String!

    }
    extend type Query {
        proveedorByUsername(name_company: String!): Proveedor
    }
    extend type Mutation {
        createProveedor(proveedor: ProveedorInput!): Proveedor
    }

`;
module.exports = proveedorTypeDefs;