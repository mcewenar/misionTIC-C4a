<template>
    <div class="page-product">
        <div class="columns is-multiline">
            <div class="column is-9">
                <figure class="image mb-6" v-if ="product.photos!=null">
                    <div  v-for="photo in product.photos" :key="photo.id">
                        <img v-bind:src="photo.image" style="width: 600px;" >
                    </div>
                </figure>

                <h1 class="title">{{ product.name_product }}</h1>

                <p>{{ product.description }}</p>
            </div>

            <div class="column is-3">
                <h2 class="subtitle">Information</h2>

                <p><strong>Price: </strong>${{ product.price }}</p>
                <p><strong>In Stock: </strong>{{ product.stock }}</p>
                <p><strong>Category: </strong>{{ product.type_product }}</p>
                <div class="field has-addons mt-6">
                    <div class="control">
                        <input type="number" class="input" min="1" v-model="quantity">
                    </div>

                    <div class="control">
                        <a class="button is-dark" @click="addToCart()">Add to cart</a>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios'
import { toast } from 'bulma-toast'

export default {
    name: 'Product',
    data() {
        return {
            product: {},
            quantity: 1
        }
    },
    mounted() {
        this.getProduct() 
    },
    methods: {
        async getProduct() {
            this.$store.commit('setIsLoading', true)
            const product_slug = this.$route.params.product_slug

            console.log(product_slug)
            axios({
                    url: 'https://apigateway-nous.herokuapp.com/',
                    method: 'post',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    data: {
                        query: `
                        query ProductById($productsId: Int!) {
                            productById(products_id: $productsId) {
                                id_products
                                name_product
                                description
                                price
                                stock
                                type_product
                                photos {
                                    image
                                }
                            }
                        }
                        `,
                        variables: {
                            productsId: parseInt(product_slug)
                        }
                    }
                }).then((result) => {
                    this.product = result.data.data.productById
                    document.title = this.product.name_product + ' | Nous'
                    console.log(result.data)
                })
                .catch(error => {
                    console.log(error)
                })
            
            this.$store.commit('setIsLoading', false)
        },
        addToCart() {
            if (isNaN(this.quantity) || this.quantity < 1) {
                this.quantity = 1
            }

            const item = {
                product: this.product,
                quantity: this.quantity
            }

            this.$store.commit('addToCart', item)

            toast({
                message: 'The product was added to the cart',
                type: 'is-success',
                dismissible: true,
                pauseOnHover: true,
                duration: 2000,
                position: 'bottom-right',
            })
        }
    }
}
</script>