const { gql } = require('apollo-server');
const authTypeDefs = gql `
    type Tokens {
        refresh: String!
        access: String!
    }
    type Access {
        access: String!
    }
    input CredentialsInput {
        username: String!
        password: String!
    }
    input SignUpInput {
        username: String!
        password: String!
        name: String!
        email: String!
    }
    type UserDetail {
        id: Int!
        username: String!
        password: String!
        name: String!
        email: String!
    }
    type Mutation {
    }
    type Query {
        userDetailById(userId: Int!): UserDetail!
    }`;
module.exports = authTypeDefs;