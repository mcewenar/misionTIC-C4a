//Se llama al typedef (esquema) de cada submodulo
//const accountTypeDefs = require('./account_type_defs');
//const transactionTypeDefs = require('./transaction_type_defs');
const authTypeDefs = require('./auth_type_defs');
const facturaTypeDefs = require('./factura_type_defs');
//Se unen
const schemasArrays = [authTypeDefs, facturaTypeDefs];
//Se exportan
module.exports = schemasArrays;

//module.exports = authTypeDefs