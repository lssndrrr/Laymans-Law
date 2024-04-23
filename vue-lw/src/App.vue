
<template>
    <div class="box-border bg-none w-[960px] h-[1080px]">
        <div class="relative flex-1 w-[960px] h-[1080px]" :style={'background-image': 'url(../assets/reddark.png)'}>
        </div>
        <div class="flex items-center justify-center flex-1 w-[960px] h-[1080px] blue">
        </div>
    </div>
    


    <RouterView />
</template>

<style>
    .redbg {
        background-image: url('@/assets/reddark.png');
        background-size: cover;
    }

    .bluebg {
        background-image: url('@/assets/bluedark.png');
        background-size: cover;
    }
</style>