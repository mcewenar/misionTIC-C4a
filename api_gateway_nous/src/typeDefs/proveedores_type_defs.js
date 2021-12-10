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
    type ProveedorUpdate {
        idRegister: Int
        name_company: String
        name_contact: String
        cel: Int
        address: String
        city: String
        email: String

    }

    extend type Query {
        proveedorById(idRegister: Int): Proveedor!
        proveedorAll(allProvider: Proveedor!): [Proveedor!]
    }
    extend type Query {
        
    }
    extend type Mutation {
        createProveedor(proveedor: Proveedor!): Proveedor
        updateProveedor(proveedor: Proveedor!): Proveedor
        deleteProveedor(name_company:String!): String
    }

`;
module.exports = proveedorTypeDefs;