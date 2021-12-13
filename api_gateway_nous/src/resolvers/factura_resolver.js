const facturaResolver = {
    Query: {
        facturaByUsername: async(_,{username}, {dataSources, userIdToken}) => {
            usernameToken = (await dataSources.authAPI.getUser(userIdToken)).username
            if (username == usernameToken)
                return dataSources.facturaApi.facturaByUsername(username)
            else
                return null
        },
    },
    Mutation: {
        createFactura: async(_, { factura }, { dataSources, userIdToken }) => {
            usernameToken = (await dataSources.authAPI.getUser(userIdToken)).username
            if (factura.username == usernameToken)
                return dataSources.facturaApi.createFactura(factura)
            else
                return null
        },
    }
};

module.exports = facturaResolver;