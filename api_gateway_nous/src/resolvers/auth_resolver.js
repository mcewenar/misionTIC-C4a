const userResolver = {
    Query: {
        userDetailById: async (_,{userId},{dataSources,userIdToken}) => {
            if (userId==userIdToken)
                return await dataSources.AuthAPI.getUser(userId)
            else
                return null
        }
    },
    Mutation: {
        signUpUser: async (_,{userInput}, {dataSources}) => {
            const authInput = {
                username: userInput.username,
                password: userInput.password,
                name: userInput.name,
                email: userInput.email
            }
            return await dataSources.AuthAPI.createUser(userInput)
        },
        logIn: async (_,{ credentials }, { dataSources }) => {
            return await dataSources.AuthAPI.authRequest(credentials)
        },
        refreshToken: (_,{ token }, {dataSources}) => 
            dataSources.AuthAPI.refreshToken(token)

    }

}

module.exports = userResolver