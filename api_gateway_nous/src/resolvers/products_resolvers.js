const ProductResolver = {
    Query: {
        productsByType: async (_, { type_product }, { dataSources }) => {
            return await dataSources.productAPI.productsByType(type_product)
        },
        productPhotos: async (_, { products_id }, { dataSources }) => {
            return await dataSources.productAPI.productsPhotos(products_id)            
        },
        productsTypes: async (_, { },{ dataSources }) => {
            return await dataSources.productAPI.productsTypes()
        },
        productById: async (_, { products_id }, { dataSources }) => {
            return await dataSources.productAPI.productById(products_id)
        },
    },
    Mutation: {
        createProduct: async (_, { product }, { dataSources, userIdToken }) => {
            // usernameToken = (await dataSources.authAPI.getUser(userIdToken)).username
            //if (transaction.usernameOrigin == usernameToken)
            return dataSources.productAPI.createProduct(product)
            //else
            //    return null
        },

        createType: async (_, { type }, { dataSources, userIdToken }) => {
            return dataSources.productAPI.createType(type)
        }
    }
};
module.exports = ProductResolver;