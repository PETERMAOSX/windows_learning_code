package com.example.application04;

import androidx.lifecycle.MutableLiveData;
import androidx.lifecycle.SavedStateHandle;
import androidx.lifecycle.ViewModel;

public class ViewModelTest extends ViewModel {
    //public MutableLiveData<Integer> myitem;
    private SavedStateHandle handle;
    public ViewModelTest(SavedStateHandle handle){
        this.handle = handle;
    }
    public MutableLiveData<Integer> getMyitem() {
        if(!handle.contains(MainActivity.KEY_NUMBER)){
            handle.set(MainActivity.KEY_NUMBER,0);
        }
        return handle.getLiveData(MainActivity.KEY_NUMBER);
//        if(this.myitem == null){
//            this.myitem = new MutableLiveData<>();
//            this.myitem.setValue(0);
//        }
//        return myitem;
    }
    public void Add(){
        getMyitem().setValue(getMyitem().getValue()+1);
        //this.myitem.setValue(this.myitem.getValue()+1);
    }
}

