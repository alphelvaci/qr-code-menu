<template>
<body>
<div id="app">
  <center class="header-container">
    <img src="http://cdn.agbdining.com/resources/midpoint.png" class="headerLogoImage">
  </center>
  <div v-if="cartOpen == false && orderFormOpen == false">
    <div class="scrollmenu">
        <a v-for="category in categories"
        v-bind:key="category.id"
        v-bind:href="'#'+category">{{ category }}</a>
    </div>
    <div v-for="category in categories" v-bind:key="category.id">
      <h3 v-bind:id="category">{{ category }}</h3>
      <li class="list" v-for="product in products" v-bind:key="product.idx">
        <product @AddToCart="openOrderForm"
        v-if="category == product.category"
        v-bind:product="product"/>
      </li>
    </div>
  </div>
  <div v-if="orderFormOpen == true">
    <order-form @Confirm="confirmOrder" @Cancel="cancelOrder" v-bind:product="inOrderForm"/>
  </div>
  <div v-if="cartOpen == true">
    <cart @CloseCart="closeCart" @RemoveFromCart="removeFromCart" v-bind:orders="inCart"/>
  </div>
  <button class="Cart-button" v-on:click="cartOpen = true"
  v-if="cartOpen == false && orderFormOpen == false">
    <img class="Cart-image" src=https://cdn.agbdining.com/resources/cart.svg>
  </button>
</div>
</body>
</template>

<script>
import axios from 'axios';
import Product from './components/Product.vue';
import Cart from './components/Cart.vue';
import OrderForm from './components/OrderForm.vue';

export default {
  name: 'App',
  components: {
    Product,
    Cart,
    OrderForm,
  },
  methods: {
    openOrderForm(product) {
      this.inOrderForm = product;
      this.orderFormOpen = true;
    },
    removeFromCart(order) {
      const index = this.inCart.indexOf(order);
      if (this.inCart[index].noOfProducts === 1) {
        this.inCart.splice(index, 1);
      } else {
        this.inCart[index].noOfProducts -= 1;
      }
    },
    confirmOrder(product, noOfProducts, orderNote) {
      let done = false;
      for (let index = 0; index < this.inCart.length; index += 1) {
        const order = this.inCart[index];
        if (order.product === product && order.orderNote === orderNote) {
          this.inCart[index].noOfProducts += noOfProducts;
          done = true;
        }
      }
      if (!done) {
        this.inCart.push({ product, noOfProducts, orderNote });
      }
      this.inOrderForm = null;
      this.orderFormOpen = false;
    },
    cancelOrder() {
      this.inOrderForm = null;
      this.orderFormOpen = false;
    },
    closeCart() {
      this.cartOpen = false;
    },
  },
  data() {
    return {
      products: null,
      categories: ['Kahvaltı', 'Burger', 'Makarna', 'Tatlılar', 'İçecekler'],
      inCart: [], // {product: product, noOfProducts: noOfProducts, orderNote: orderNote}
      cartOpen: false,
      inOrderForm: null,
      orderFormOpen: false,
    };
  },
  mounted() {
    axios.get('http://api.agbdining.com/api/v1/products')
      .then((response) => { (this.products = response.data); });
  },
};
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

.Cart-button {
  height: 60px;
  width: 60px;
  display: flex;
  border-radius: 50%;
  border-color: rgba(255, 255, 255, 0);
  background-color: rgb(199, 199, 199);
  box-shadow: 2px 2px 5px rgba(168, 168, 168, 0.747);
  position: fixed;
  bottom: 30px;
  right: 30px;
}

.Cart-button:hover {
  background-color: #444;
}

.Cart-image {
  height: 30px;
  margin-top: 2px;
}

</style>
