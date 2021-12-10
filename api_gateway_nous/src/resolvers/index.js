const authResolver = require('./auth_resolver')
const providerResolver = require('./proveedore_resolver')
const lodash = require('lodash')

const resolvers = lodash.merge(authResolver,providerResolver)
module.exports = resolvers
