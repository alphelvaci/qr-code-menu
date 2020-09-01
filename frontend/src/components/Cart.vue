<template>
<div class="Cart">
  <div class="Cart-header">
    <button class="Close-button" v-on:click="closeCart">
      <img class="Cross-image" src=https://cdn.agbdining.com/resources/cross.svg>
    </button>
    <h2 class="Cart-title">Sepetim</h2>
  </div>
  <div class="list" v-for="order in orders" v-bind:key="order.idx">
    <product-in-cart @RemoveFromCart="removeFromCart(order)" v-bind:product="order.product"/>
    <div class="Info">
    <h3 class="Count">{{ order.noOfProducts }} Adet</h3>
    <h4 class="Note" v-if="order.orderNote">Not: {{ order.orderNote }}</h4>
    </div>
  </div>
</div>
</template>

<script>
import ProductInCart from './ProductInCart.vue';

export default {
  name: 'Cart',
  components: {
    ProductInCart,
  },
  props: {
    orders: Array,
  },
  methods: {
    closeCart() {
      this.$emit('CloseCart');
    },
    removeFromCart(order) {
      this.$emit('RemoveFromCart', order);
    },
    confirmCart() {
      return null;
    },
    data() {
      return {
      };
    },
  },
};
</script>

<style>
.Cart-header {
  height: 50px;
  width: 100%;
}

.Cart-title {
  margin: auto;
  width: 100px;
}

.Info {
  display: flex;
  flex-flow: row;
  width: 100%;
}

.Count {
  flex: 1;
}

.Note {
  flex: 1;
}

.Close-button{
  height: 30px;
  width: 30px;
  display: flex;
  border-radius: 50%;
  border: 1px solid #777;
  background-color: rgb(231, 231, 231);
  margin: auto;
  margin-left: 30px;
  float: left;
  justify-content: center;
}

.Close-button:hover {
  background-color: #444;
  color:#eee;
}

.Cross-image {
  height: 15px;
}

</style>
