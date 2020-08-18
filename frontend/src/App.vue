<template>
  <div id="app">
    <li class="list" v-for="product in products" v-bind:key="product.id" list-style-type:none>
      <product v-bind:caption="product.caption" v-bind:description="product.description" v-bind:url="product.url" v-bind:price="product.price"/>
    </li>
  </div>
</template>

<script>
import Product from './components/Product.vue'

export default {
  name: 'App',
  components: {
    Product
  },
  data() {
    return {
      products: [
        {
        caption: "birinci resim",
        description: "iwdnowidnwodinwodinwo",
        url: "https://upload.wikimedia.org/wikipedia/commons/b/b6/Image_created_with_a_mobile_phone.png",
        price: 15
        },
        {
        caption: "ikinci resim",
        description: "iwdnowidnwodinwodinwo",
        url:"https://images.squarespace-cdn.com/content/v1/5a5906400abd0406785519dd/1547305835578-QAFSA9Q5TND01TZBN03B/ke17ZwdGBToddI8pDm48kKAwwdAfKsTlKsCcElEApLR7gQa3H78H3Y0txjaiv_0fDoOvxcdMmMKkDsyUqMSsMWxHk725yiiHCCLfrh8O1z5QPOohDIaIeljMHgDF5CVlOqpeNLcJ80NK65_fV7S1UegTYNQkRo-Jk4EWsyBNhwKrKLo5CceA1-Tdpfgyxoog5ck0MD3_q0rY3jFJjjoLbQ/grant3.jpg?format=2500w",
        price: 77
        },
      ]
    }
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
.list {
  list-style-type:none
}
</style>
