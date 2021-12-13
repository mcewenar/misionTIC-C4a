const { gql } = require('apollo-server');
const proveedorTypeDefs = gql `
    type Proveedor {
        idRegister: Int!
        name_company: String!
        name_contact: String!
        cel: Int!
        address: String!
        city: String!
        email: String!

    }
    input ProveedorCreate {
        name_company: String!
        name_contact: String!
        cel: Int!
        address: String!
        city: String!
        email: String!

    }

    input ProveedorUpdate {
        name_company: String
        name_contact: String
        cel: Int
        address: String
        city: String
        email: String
    }


    extend type Query {
        proveedorById(proveedor: Int!): Proveedor
    }
    extend type Mutation {
        createProveedor(proveedor: ProveedorCreate!): Proveedor
        updateProveedor(proveedor: ProveedorUpdate!): Proveedor
        deleteProveedor(idRegister: Int!): String
    }

`;
module.exports = proveedorTypeDefs;