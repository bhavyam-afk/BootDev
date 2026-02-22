import { describe, expect, test, beforeEach, afterEach, vi } from "vitest";
import { Cache } from "./pokecache";

describe("Cache", () => {
  let cache: Cache;

  beforeEach(() => {
    cache = new Cache(100); // 100ms interval
  });

  afterEach(() => {
    cache.stopReapLoop();
  });

  test("add and get should store and retrieve values", () => {
    cache.add("key1", "value1");
    expect(cache.get("key1")).toBe("value1");
  });

  test("get should return undefined for missing keys", () => {
    expect(cache.get("nonexistent")).toBeUndefined();
  });

  test("should support generic types", () => {
    const obj = { name: "test", id: 123 };
    cache.add("obj", obj);
    expect(cache.get("obj")).toEqual(obj);
  });

  test("should delete expired entries after interval", async () => {
    cache.add("expiring", "value");
    expect(cache.get("expiring")).toBe("value");

    // Wait 250ms to ensure reap runs (interval is 100ms)
    await new Promise(resolve => setTimeout(resolve, 250));
    
    expect(cache.get("expiring")).toBeUndefined();
  });

  test("should keep recent entries", async () => {
    cache.add("recent", "value");

    // Wait 50ms then add a newer entry
    await new Promise(resolve => setTimeout(resolve, 50));
    cache.add("newer", "newer_value");
    
    // Wait another 150ms (total 200ms from start)
    await new Promise(resolve => setTimeout(resolve, 150));
    
    // "recent" should be reaped but "newer" should still exist
    expect(cache.get("recent")).toBeUndefined();
    expect(cache.get("newer")).toBe("newer_value");
  });
});
