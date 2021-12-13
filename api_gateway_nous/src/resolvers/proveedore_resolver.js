const providerResolver = {
    Query: {
        proveedorById: async(_,{userInput}, {dataSources,userIdToken}) => {
            return await dataSources.ProveedorAPI.getProviderByName(userInput)
        }
        //proveedorAll: async(_,{userInput}, {dataSources,userIdToken}) => {
        //    return await dataSources.ProveedorAPI.getAllProvider(userInput)
        //}
    },
    Mutation: {
        createProveedor: async(_,{proveedor}, {dataSources,userIdToken}) => {
            return await dataSources.ProveedorAPI.createProvider(proveedor)

        },
        updateProveedor: async(_,{proveedorId}, {dataSources,userIdToken}) => {
            return await dataSources.ProveedorAPI.updateProvider(proveedorId)
        },
        deleteProveedor: async(_,{proveedorId}, {dataSources,userIdToken}) => {
            return await dataSources.ProveedorAPI.deleteProvider(proveedorId)
        }
    }

}

module.exports = providerResolver