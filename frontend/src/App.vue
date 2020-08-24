<template>
<body>
<div id="app">
	<li class="list" v-for="product in products" v-bind:key="product.idx" list-style-type:none>
		<product v-bind:caption="product.name" v-bind:description="product.description" v-bind:url="'http://cdn.agbdining.com/' + product.imageUrl" v-bind:price="product.price"/>
	</li>
</div>
</body>
</template>

<script>
import Product from './components/Product.vue'
import axios from 'axios'

export default {
  name: 'App',
  components: {
    Product
  },
  data() {
    return {
      products: null
    }
  },
  mounted() {
    axios.get('http://api.agbdining.com/api/v1/products')
      .then((response) => (this.products = response.data))
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
