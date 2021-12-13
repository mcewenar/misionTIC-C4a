const { RESTDataSource } = require('apollo-datasource-rest');
const serverConfig = require('../server');

class FacturaApi extends RESTDataSource {
    constructor(){
        super();
        this.baseURL = serverConfig.facturas_api_url;
    }
    async createFactura(factura) {
        factura = new Object(JSON.parse(JSON.stringify(factura)));
        return await this.post('/factura/',factura);
    }
    async facturaByUsername(username){
        return await this.get(`/factura/${username}/`);
    }

}

module.exports = FacturaApi;