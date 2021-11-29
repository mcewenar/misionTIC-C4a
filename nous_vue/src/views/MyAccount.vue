<template>
    <div class="page-my-account">
        <div class="columns is-multiline">
            <div class="column is-12">
                <h1 class="title">Mi Cuenta</h1>
            </div>

            <div class="column is-12">
                <button @click="logout()" class="button is-danger">Deslogueate</button>
            </div>

            <hr>

            <div class="column is-12">
                <h2 class="subtitle">Mis ordenes</h2>

                <OrderSummary
                    v-for="order in orders"
                    v-bind:key="order.id"
                    v-bind:order="order" />
            </div>
        </div>
    </div>
</template>

<script>
import OrderSummary from '@/components/OrderSummary.vue'

export default {
    name: 'MyAccount',
    components: {
        OrderSummary
    },
    data() {
        return {
            orders: []
        }
    },
    mounted() {
        document.title = 'Mi Cuenta | Nous'

        this.getMyOrders()
    },
    methods: {

    }
}
</script>