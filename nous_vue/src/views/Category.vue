<template>
    <div class="page-category">
        <div class="columns is-multiline">
            <div class="column is-12">
                <h2 class="is-size-2 has-text-centered">{{ category.name }}</h2>
            </div>

            <ProductBox 
                v-for="product in products"
                v-bind:key="product.products_id"
                v-bind:product="product" />
        </div>
    </div>
</template>

<script>
import axios from 'axios'
import { toast } from 'bulma-toast'

import ProductBox from '@/components/ProductBox'

export default {
    name: 'Category',
    components: {
        ProductBox
    },
    data() {
        return {
            category: {},
            products: []
            
        }
    },
    mounted() {
        this.getCategory()
    },
    watch: {
        $route(to, from) {
            if (to.name === 'Category') {
                this.getCategory()
            }
        }
    },
    methods: {
        async getCategory() {
            const categorySlug = this.$route.params.category_slug

            this.$store.commit('setIsLoading', true)

            axios({
                    url: 'https://apigateway-nous.herokuapp.com/',
                    method: 'post',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    data: {
                        query: `
                        query ProductsByType($typeProduct: Int!) {
                            productsByType(type_product: $typeProduct) {
                                id_products
                                name_product
                                description
                                photos{ 
                                    image
                                    }
                                price
                                stock
                                type_product
                            }
                        }
                        `,
                        variables: {
                            typeProduct: parseInt(categorySlug)
                        }
                    }
                }).then((result) => {
                    //document.title = this.category.name + ' | Nous'
                    this.products = result.data.data.productsByType                    
                    
                    console.log(result.data)
                })
                .catch(error => {
                    console.log(error)

                    toast({
                        message: 'Something went wrong. Please try again.',
                        type: 'is-danger',
                        dismissible: true,
                        pauseOnHover: true,
                        duration: 2000,
                        position: 'bottom-right',
                    })
                })

            this.$store.commit('setIsLoading', false)
        }
    }
}
</script>