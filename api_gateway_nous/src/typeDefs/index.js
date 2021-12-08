//Se llama al typedef (esquema) de cada submodulo
//const transactionTypeDefs = require('./transaction_type_defs');
const authTypeDefs = require('./auth_type_defs');
const proveedorTypeDefs = require('./proveedores_type_defs');
//Se unen
const schemasArrays = [authTypeDefs, proveedorTypeDefs];
//Se exportan
module.exports = schemasArrays