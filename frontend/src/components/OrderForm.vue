<template>
<div class="OrderForm">
    <product-in-order-form v-bind:product="product"/>
    <h3 class="orderNote">
        Notunuz:
    </h3>
    <h3 class="noOfProducts">
        Adet:
        <button class="addRemoveButton" v-on:click="remove">Çıkar</button>
        {{ noOfProducts }}
        <button class="addRemoveButton" v-on:click="noOfProducts += 1">Ekle</button>
    </h3>
    <input v-model="orderNote"/>
    <button class="confirmationButton" v-on:click="cancel">Iptal</button>
    <button class="confirmationButton" v-on:click="confirm">Onayla</button>
</div>
</template>

<script>
import ProductInOrderForm from './ProductInOrderForm.vue';

export default {
  name: 'OrderForm',
  components: {
    ProductInOrderForm,
  },
  props: {
    product: Object,
  },
  methods: {
    remove() {
      if (this.noOfProducts !== 1) {
        this.noOfProducts -= 1;
      }
    },
    confirm() {
      this.$emit('Confirm', this.product, this.noOfProducts, this.orderNote);
    },
    cancel() {
      this.$emit('Cancel');
    },
  },
  data() {
    return {
      noOfProducts: 1,
      orderNote: null,
    };
  },
};
</script>

<style>

.orderNote {
    float: left;
    margin-left: 5%;
}

.noOfProducts {
    float: right;
    margin-right: 5%;
}

.addRemoveButton {
  height: 25px;
  width: 55px;
  background-color: rgb(231, 231, 231);
  border: 1px solid #777;
  border-radius: 5px;
}

.addRemoveButton:hover {
  background-color: #444;
  color:#eee;
}

.confirmationButton {
    margin-top: 20px;
    height: 45px;
  width: 45%;
  background-color: rgb(231, 231, 231);
  border: 1px solid #777;
  border-radius: 5px;
}

.confirmationButton:hover {
    background-color: #444;
  color:#eee;
}

input{
    width: 89%;
    height: 20px;
    border: 1px solid grey;
}

</style>
