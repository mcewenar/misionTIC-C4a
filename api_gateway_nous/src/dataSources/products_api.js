const { RESTDataSource } = require('apollo-datasource-rest');
const serverConfig = require('../server');
class ProductAPI extends RESTDataSource {
    constructor() {
        super();
        this.baseURL = serverConfig.products_api_url;
    }
    async createProduct(product) {
        product = new Object(JSON.parse(JSON.stringify(product)));
        return await this.post('/products', product);
    }
    async createType(type) {
        type = new Object(JSON.parse(JSON.stringify(type)));
        return await this.post('/types', type);
    }
    async productById(products_id) {
        let products = await this.get(`/products?id_products=${products_id}`)        
        let photos = await this.productsPhotos(products[0].id_products)        
        
        products[0].photos = photos        
        
        return products[0]
    }
    async productsByType(type_product) {
        let products = await this.get(`/products?type_product=${type_product}`)
        let promises = []

        products.forEach( (product, index) => {            
            
            promises.push(
                this.productsPhotos(product.id_products).then(photos => {
                    products[index].photos = photos
                })
            )
            
        })
        await Promise.all( promises )
        return products       
    }
    async productsPhotos(product_id) {
        return await this.get(`/photos?product=${product_id}`);
    }
    async productsTypes() {
        return await this.get(`/types`);
    }
    
    
}
module.exports = ProductAPI;