package com.smartwecs.com.awslibrary;

/**
 * Callback async operations.
 * @param <R>
 */
public interface awsCallback<R> {

    void onResult(R result);

    void onError(Exception e);
}

