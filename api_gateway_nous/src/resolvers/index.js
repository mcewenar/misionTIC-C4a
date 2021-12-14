const productResolver = require('./products_resolvers');
const authResolver = require('./auth_resolver');
const lodash = require('lodash');
const resolvers = lodash.merge(productResolver, authResolver);
module.exports = resolvers;