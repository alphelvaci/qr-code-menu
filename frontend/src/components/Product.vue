<template>
    <div style="width: 100%; display: table">
        <div style="display: table-row; height: 100px;">
            <div style="width: 33%; display: table-cell">
                <img v-bind:src="url" height="50px" width="50px">
            </div>
            <div style="width: 33%; display: table-cell">
                {{ caption }} <br>
                {{ description }}
            </div>
            <div style="display: table-cell"> 
                {{ price }}
            </div>
        </div>
    </div>
</template>

<script>
export default {
    name: 'Product',
    props:  {
        caption: String,
        url: String,
        description: String,
        price: Float32Array
    }

}
</script>

<style>

</style>
