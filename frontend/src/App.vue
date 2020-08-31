<template>
<body>
<div id="app">
  <center class="header-container">
    <img src="http://cdn.agbdining.com/resources/midpoint.png" class="headerLogoImage">    
  </center>
  <div class="scrollmenu">
      <a v-for="category in categories" v-bind:key="category.id" v-bind:href="'#'+category">{{ category }}</a>
  </div>
  <div v-for="category in categories" v-bind:key="category.id">
    <h3 v-bind:id="category">{{ category }}</h3>
    <li class="list" v-for="product in products" v-bind:key="product.idx">
      <product v-if="category == product.category" v-bind:product="product"/>
    </li>
  </div>
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
  methods: {
    addToCart: function (product) {
      this.inCart.push(product)
    }
  },
  data() {
    return {
      products: null,
      categories: ['Kahvaltı', 'Burger', 'Makarna', 'Tatlılar', 'İçecekler'],
      inCart: [],
      cartOpen: false
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
  margin: 0px;
  padding:0px;
}

html {
  scroll-behavior:smooth
}

body {
margin: 0px;
  padding:0px;
}

.list {
  list-style-type:none
}

.headerLogoImage {
	height: 80px;
	background-color: #fff;
}

div.scrollmenu {
	padding-top: 3px;
	padding-bottom: 3px;
	background-color: #777;
	overflow: scroll;
	white-space: nowrap;
}

 ::-webkit-scrollbar {
	width: 0px;
	height: 0px;
}

div.scrollmenu a {
	display: inline-block;
	border-radius: 3px;
	background-color:rgb(231, 231, 231);
	width: 135px;
	color: #777;
	text-align: center;
	padding: 14px;
	text-decoration: none;
	margin-left: 2px;
	margin-right: 1px;
}

div.scrollmenu a:hover {
	background-color: #444;
  color:#eee;
}
</style>
